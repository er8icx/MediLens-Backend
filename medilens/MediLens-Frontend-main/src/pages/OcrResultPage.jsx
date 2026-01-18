import { useLocation } from "react-router-dom";
import ChatBot from "../components/ChatBot";
import "../css/Navbar.css";
import "../css/OcrResultPage.css";

function OcrResultPage() {
  const location = useLocation();
  const { image, medicineName } = location.state || {};

  return (
    <>
      <div className="navbar">MediLens</div>

      <div className="medicine-page">
        <div className="medicine-content">
          <h2>{medicineName || "OCR Result"}</h2>

          {image && (
            <img
              src={image}
              alt="OCR"
              className="ocr-image"
            />
          )}

          <p>Failed to load medicine summary.</p>
        </div>

        <div className="medicine-chatbot">
          <ChatBot medicineName={medicineName} />
        </div>
      </div>
    </>
  );
}

export default OcrResultPage;
