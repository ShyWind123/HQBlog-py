from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage

#星火认知大模型Spark3.5 Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v3.5/chat'
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v1.1/chat'
#星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
# 3.5
SPARKAI_APP_ID = '34458b5c'
SPARKAI_API_SECRET = 'ZjNlOTU5OTBlNDIxODdjMjU3MjcyMzli'
SPARKAI_API_KEY = '549d2240bc0196d82fb1ac4e16079be9'
#星火认知大模型Spark3.5 Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_DOMAIN = 'generalv3.5'
SPARKAI_DOMAIN = 'general'

def generateConclusion(content):
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    messages = [ChatMessage(
        role="system",
        content="根据我给出的文章进行总结，只给出总结的内容，不要有废话，生成总结的字数大约在原文章字数的10%左右。每次独立生成。"
    ),
    ChatMessage(
        role="user",
        content=content
    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    res = a.generations[0][0].text
    print(res)
    return res