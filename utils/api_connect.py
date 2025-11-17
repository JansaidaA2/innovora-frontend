import requests
import os

# ✅ Backend URL - Use Render in production, localhost for development
BACKEND_URL = os.getenv("BACKEND_URL", "https://innovora-backend.onrender.com")

# Alternative: Uncomment this line to force localhost for testing
# BACKEND_URL = "http://127.0.0.1:5000"


def generate_image_api(payload: dict, files=None):
    """
    Sends a POST request to the Flask backend to generate an image
    based on the user's brand info and text prompt.
    
    Args:
        payload: Dictionary with 'prompt' key
        files: Optional files dictionary for brand logo upload
        
    Returns:
        JSON response from backend
    """
    try:
        print(f"🌐 Connecting to: {BACKEND_URL}")
        print(f"📝 Prompt: {payload.get('prompt', '')[:100]}...")
        
        if files:
            # Convert file bytes into form-data for upload
            file_data = {"image": ("brand_logo.png", files["brand_logo"], "image/png")}
            response = requests.post(
                f"{BACKEND_URL}/api/avatar/generate",
                files=file_data,
                data={"prompt": payload.get("prompt", "")},
                timeout=120
            )
        else:
            # Normal text-only generation
            response = requests.post(
                f"{BACKEND_URL}/api/image/generate",
                json={"prompt": payload.get("prompt", "")},
                timeout=120
            )

        response.raise_for_status()
        result = response.json()
        
        # Fix relative URLs to absolute URLs
        if result.get("status") == "success" and "results" in result:
            openai_url = result["results"].get("openai", "")
            
            # If URL is relative, make it absolute
            if openai_url and openai_url.startswith("/static/"):
                result["results"]["openai"] = f"{BACKEND_URL}{openai_url}"
                print(f"✅ Image URL: {result['results']['openai']}")
        
        return result

    except requests.exceptions.ConnectionError:
        return {
            "status": "error", 
            "error": f"Backend not reachable at {BACKEND_URL}. Please ensure Flask is running."
        }
    except requests.exceptions.Timeout:
        return {"status": "error", "error": "Request timed out. Try again later."}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "error": str(e)}


def generate_video_api(text: str, style: str = "business", background: str = "professional"):
    """
    Generate professional avatar video via backend API
    
    Args:
        text: Text for avatar to speak
        style: Video style (business, casual, etc.)
        background: Background type (professional, gradient, etc.)
        
    Returns:
        JSON response with video URL
    """
    try:
        print(f"🌐 Connecting to: {BACKEND_URL}")
        print(f"🎬 Generating video with text: {text[:50]}...")
        
        response = requests.post(
            f"{BACKEND_URL}/api/video/generate",
            json={
                "text": text,
                "style": style,
                "background": background
            },
            timeout=300  # 5 minutes for video generation
        )
        
        response.raise_for_status()
        result = response.json()
        
        # Fix relative URLs to absolute URLs
        if result.get("status") == "success" and "video_url" in result:
            video_url = result["video_url"]
            
            # If URL is relative, make it absolute
            if video_url and video_url.startswith("/static/"):
                result["video_url"] = f"{BACKEND_URL}{video_url}"
                print(f"✅ Video URL: {result['video_url']}")
        
        return result
        
    except requests.exceptions.ConnectionError:
        return {
            "status": "error", 
            "error": f"Backend not reachable at {BACKEND_URL}. Please ensure Flask is running."
        }
    except requests.exceptions.Timeout:
        return {
            "status": "error", 
            "error": "Request timed out. Video generation takes 1-3 minutes on free tier, please try again."
        }
    except requests.exceptions.RequestException as e:
        return {"status": "error", "error": str(e)}


def check_backend_health():
    """
    Check if backend is online and reachable
    Uses quick timeout - if it fails, backend might just be cold starting
    
    Returns:
        dict: {"status": bool, "message": str, "response_time": float}
    """
    import time
    start_time = time.time()
    
    try:
        # Quick check with 5 second timeout
        response = requests.get(f"{BACKEND_URL}/health", timeout=5)
        response_time = time.time() - start_time
        
        if response.status_code == 200:
            print(f"✅ Backend is online at {BACKEND_URL} ({response_time:.2f}s)")
            return {
                "status": True, 
                "message": "Online", 
                "response_time": response_time
            }
        else:
            print(f"⚠️ Backend returned status {response.status_code}")
            return {
                "status": False, 
                "message": f"Status {response.status_code}", 
                "response_time": response_time
            }
            
    except requests.exceptions.Timeout:
        print(f"⏱️ Health check timed out - backend may be cold starting (this is normal)")
        return {
            "status": None,  # Unknown status
            "message": "Cold start (wait 50s)", 
            "response_time": 5.0
        }
        
    except requests.exceptions.ConnectionError:
        print(f"❌ Cannot connect to backend at {BACKEND_URL}")
        return {
            "status": False, 
            "message": "Connection failed", 
            "response_time": 0
        }
        
    except Exception as e:
        print(f"❌ Backend health check failed: {str(e)}")
        return {
            "status": False, 
            "message": str(e)[:50], 
            "response_time": 0
        }


# Test function
if __name__ == "__main__":
    print("=" * 60)
    print("🧪 Testing Innovora Backend Connection")
    print("=" * 60)
    
    # Check backend health
    print("\n1️⃣ Checking backend health...")
    is_healthy = check_backend_health()
    
    if is_healthy:
        print("\n2️⃣ Testing image generation...")
        result = generate_image_api({"prompt": "A test image of a robot"})
        print(f"Result: {result}")
        
        # Uncomment to test video (takes 1-3 minutes)
        # print("\n3️⃣ Testing video generation...")
        # video_result = generate_video_api("Hello world")
        # print(f"Result: {video_result}")
    else:
        print("\n❌ Backend is not accessible. Please check the URL.")