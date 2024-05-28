from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sparkAPI import generateConclusion

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#前端中生成数据请求响应
@app.post('/blogs/generate_conclusion')
async def generate_and_send_data(blogContent: dict):
    try:
        res = generateConclusion(blogContent["content"])
        return {
            "message": "Successfully generated conclusion",
            "conclusion": res
        }
    except Exception as e:
        return {"error": f"Failed to generate conclusion: {str(e)}"}
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=2001)