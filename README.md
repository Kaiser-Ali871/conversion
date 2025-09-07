# Base64 to Binary Image API

This API converts Base64 strings to binary image files and returns them via an HTTP POST endpoint.

## Usage

### Endpoint
POST `/base64-to-image/`

### Request JSON
```json
{
  "filename": "image.png",
  "image_base64": "iVBORw0KGgoAAAANSUhEUgAA..."
}
