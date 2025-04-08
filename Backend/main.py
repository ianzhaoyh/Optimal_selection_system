from fastapi import FastAPI
from back.api import router

app = FastAPI(
    title="Optimal Selection System API",
    version="1.0"
)

# 挂载所有路由
app.include_router(router)

# 运行方式（终端执行）：
# uvicorn back.main:app --reload