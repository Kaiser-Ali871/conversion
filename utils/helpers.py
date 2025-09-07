def infer_mime_type(filename: str) -> str:
    """
    Infer MIME type from filename extension
    """
    filename = filename.lower()
    if filename.endswith(".png"):
        return "image/png"
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        return "image/jpeg"
    elif filename.endswith(".gif"):
        return "image/gif"
    else:
        return "application/octet-stream"
