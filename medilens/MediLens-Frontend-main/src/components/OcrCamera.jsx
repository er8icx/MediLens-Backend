import { useNavigate } from "react-router-dom";

function OcrCamera() {
  const navigate = useNavigate();

  const handleImageUpload = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const imageUrl = URL.createObjectURL(file);

    // 🔴 DEMO detected medicine (backend will replace later)
    const detectedMedicine = "paracetamol";

    navigate("/ocr-result", {
      state: {
        image: imageUrl,
        medicineName: detectedMedicine,
      },
    });
  };

  return (
    <div className="tool-card">
      <div className="tool-header">OCR Camera</div>

      <div className="tool-body tool-camera">
        <label className="camera-button">
          📷
          <input
            type="file"
            accept="image/*"
            hidden
            onChange={handleImageUpload}
          />
        </label>
      </div>

      <p className="ocr-hint">Click the camera to upload an image</p>
    </div>
  );
}

export default OcrCamera;
