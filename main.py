from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sparkAPI import generateConclusion, generateTags

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 前端中生成数据请求响应
@app.post('/blogs/generate_conclusion')
async def generateConclusionData(blogContent: dict):
    try:
        res = generateConclusion(blogContent["content"])
        return {
            "message": "成功生成总结!",
            "conclusion": res
        }
    except Exception as e:
        return {"error": f"生成总结失败：{str(e)}"}

# 前端中生成数据请求响应
@app.post('/blogs/generate_tags')
async def generateTagsData(blogContent: dict):
    try:
        res = generateTags(blogContent["content"])
        return {
            "message": "成功生成标签!",
            "tags": res
        }
    except Exception as e:
        return {"error": f"生成标签失败：{str(e)}"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=2001)