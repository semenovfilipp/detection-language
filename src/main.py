import detectlanguage
from mlp_sdk.abstract import Task
from mlp_sdk.hosting.host import host_mlp_cloud
from mlp_sdk.transport.MlpServiceSDK import MlpServiceSDK
from pydantic import BaseModel, Field

"""
Data Class который отвечает за запрос из Caila.io
Наследуемся от BaseModel что бы сделать свой класс, который можно будет использовать в predict
"""
class PredictRequest(BaseModel):
    query: str


# Data Class который отвечает за ответ от detectlanguage
class LanguageDetection(BaseModel):
    language: str
    isReliable: bool
    confidence: float


"""
Data Class который отвечает за ответ в Caila.io
Наследуемся от BaseModel что бы сделать свой класс, который можно будет использовать в predict
"""
class PredictResponse(BaseModel):
    detections: list[LanguageDetection]

# Наследуемся от класса Task для реализации predict метода
class LanguageDetectionService(Task):

    """
    Так как мы наследуемся от класса Task, то нам , важно убедиться, что родительский класс правильно инициализирован.
     Вызов super().__init__() гарантирует, что все необходимые атрибуты родительского класса будут правильно установлены.
    """
    def __init__(self, config: BaseModel, service_sdk: MlpServiceSDK = None):
        print("Сервис запущен",end="\n\n")
        super().__init__(config, service_sdk)

    """
    Реализуем метод predict, который принимает запрос из Caila.io и возвращает ответ в Caila.io
    """
    def predict(self, data: PredictRequest, config: BaseModel) -> PredictResponse:
        print(f"1.Отправляем запрос по API  в detection-language: {data.query}")
        raw_detections = detectlanguage.detect(data.query)

        print(f"2.Получаем ответ от detection-language :"
              f"{raw_detections} ")

        print("3.Обрабатываем ответ от detection-language и формируем ответ для Caila.io", end="\n\n")
        detections = [LanguageDetection(**detection) for detection in raw_detections]

        return PredictResponse(detections=detections)


if __name__ == "__main__":
    # Устанавливаем ключ для доступа к detectlanguage
    detectlanguage.configuration.api_key = "84c1f6c668d5167c1b547350c6224211"
    # Запускаем сервис
    host_mlp_cloud(LanguageDetectionService, BaseModel())
