from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
import base64
import io
from utils.helpers import infer_mime_type

app = FastAPI(title="Base64 to Binary Image API")

# Request model
class ImageRequest(BaseModel):
    filename: str
    image_base64: str

@app.post("/base64-to-image/")
async def base64_to_image(data: ImageRequest):
    """
    Accepts a Base64 string and filename, returns the image as a streaming response.
    """
    try:
        # Decode Base64 to bytes
        img_bytes = base64.b64decode(data.image_base64)
        img_stream = io.BytesIO(img_bytes)
        img_stream.seek(0)

        # Infer MIME type based on filename
        mime_type = infer_mime_type(data.filename)

        # Return StreamingResponse so connection closes immediately
        return StreamingResponse(img_stream, media_type=mime_type)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing image: {e}")
