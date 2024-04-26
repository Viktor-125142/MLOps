import gradio as gr
from transformers import FSMTForConditionalGeneration, FSMTTokenizer

# Название модели для переводчика
model_name = "facebook/wmt19-ru-en"  # Пример модели перевода с русского на английский

# Загрузка модели и токенизатора
model = FSMTForConditionalGeneration.from_pretrained(model_name)
tokenizer = FSMTTokenizer.from_pretrained(model_name)


# Функция для выполнения перевода
def translate(text):
    # Токенизация текста для подготовки к входу в модель
    input_ids = tokenizer.encode(text, return_tensors="pt")

    # Предсказание модели
    translated = model.generate(input_ids)

    # Декодирование предсказания модели в читаемый текст
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    return translated_text


# Создание интерфейса Gradio
iface = gr.Interface(
    fn=translate,
    inputs=gr.Textbox(lines=2, placeholder="Введите текст для перевода с русского на английский"),
    outputs=["text"],
    title="Переводчик с русского на английский"
)

if __name__ == '__main__':
    iface.launch(server_port=8000)
