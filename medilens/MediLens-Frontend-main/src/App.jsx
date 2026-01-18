import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Home from "./pages/Home";
import MedicinePage from "./pages/MedicinePage";
import OcrResultPage from "./pages/OcrResultPage";

import "./css/App.css";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/home" element={<Home />} />
        <Route path="/medicine/:name" element={<MedicinePage />} />
        <Route path="/ocr-result" element={<OcrResultPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
