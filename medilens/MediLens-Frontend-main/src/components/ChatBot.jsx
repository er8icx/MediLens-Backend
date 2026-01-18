import { useEffect, useState } from "react";
import "../css/ChatBot.css";

function ChatBot({ medicineName }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  // Reset chat when medicine changes
  useEffect(() => {
    if (medicineName) {
      setMessages([
        {
          sender: "bot",
          text: `You are viewing information about "${medicineName}". Ask me anything about this medicine.`,
        },
      ]);
    }
  }, [medicineName]);

  const sendMessage = async () => {
  if (!input.trim()) return;

  const userText = input;

  setMessages(prev => [...prev, { sender: "user", text: userText }]);
  setInput("");
  setLoading(true);

  try {
    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        medicine: medicineName,
        question: userText,
      }),
    });

    const data = await res.json();

    setMessages(prev => [
      ...prev,
      { sender: "bot", text: data.answer },
    ]);
  } catch (e) {
    setMessages(prev => [
      ...prev,
      { sender: "bot", text: "Server error. Try again." },
    ]);
  } finally {
    setLoading(false);
  }
};



  return (
    <div className="tool-card">
      <div className="tool-header">Chat Bot</div>

      <div className="tool-body">
        {messages.length === 0 && (
          <div className="tool-placeholder">Messages will appear here</div>
        )}

        {messages.map((m, i) => (
          <div key={i} className={`chat-message ${m.sender}`}>
            {m.text}
          </div>
        ))}

        {loading && (
          <div className="chat-message bot">Typing…</div>
        )}
      </div>

      <div className="tool-footer">
        <input
          placeholder="Ask about this medicine..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />
      </div>
    </div>
  );
}

export default ChatBot;
