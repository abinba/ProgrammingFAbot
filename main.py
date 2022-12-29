import openai

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from telegram.ext.filters import ALL

from core.config import TELEGRAM_BOT_TOKEN, OPENAI_API_KEY
from core.texts import START_TEXT

openai.api_key = OPENAI_API_KEY


def generate_prompt(prompt: str) -> str:
    return f"""You are a programming teacher.
    Student asks you: {prompt}
    You answer:
    """


def create_response(prompt: str) -> str:
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=generate_prompt(prompt),
        temperature=0.7,
        max_tokens=100,
    )
    return response.choices[0].text


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: # noqa
    language_chosen = "en"
    await update.message.reply_markdown(START_TEXT[language_chosen].format(update.effective_user.first_name))


async def question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: # noqa
    response = create_response(update.message.text)
    await update.message.reply_text(response)


app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(ALL, question))

app.run_polling()
print("Bot is running!")

