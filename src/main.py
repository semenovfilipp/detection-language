import detectlanguage
from mlp_sdk.abstract import Task
from mlp_sdk.hosting.host import host_mlp_cloud
from mlp_sdk.transport.MlpServiceSDK import MlpServiceSDK
from pydantic import BaseModel, Field


# Data Class который отвечает за запрос из Caila.io
class PredictRequest(BaseModel):
    query: str = Field(alias="q")


# Data Class который отвечает за ответ от detectlanguage
class LanguageDetection(BaseModel):
    language: str
    isReliable: bool
    confidence: float


# Data Class который отвечает за ответ в Caila.io
class PredictResponse(BaseModel):
    detections: list[LanguageDetection]


class LanguageDetectionService(Task):
    def __init__(self, config: BaseModel, service_sdk: MlpServiceSDK = None) -> None:
        print("Сервис запущен")
        super().__init__(config, service_sdk)

    def predict(self, data: PredictRequest, config: BaseModel) -> PredictResponse:
        print("1.Отправляем запрос по API  в detection-language")
        raw_detections = detectlanguage.detect(data.query)

        print(f"2.Получаем ответ от detection-language :"
              f"{raw_detections} ")

        print("3.Обрабатываем ответ от detection-language и формируем ответ для Caila.io")
        detections = [LanguageDetection(**detection) for detection in raw_detections]
        return PredictResponse(detections=detections)


if __name__ == "__main__":
    detectlanguage.configuration.api_key = "84c1f6c668d5167c1b547350c6224211"
    host_mlp_cloud(LanguageDetectionService, BaseModel())
