"""
The chat interface: a simple terminal loop.

Run it:
    poetry run python -m app.main

Make sure you've built the index at least once first:
    poetry run python -m app.ingest

Type `exit` (or `quit`) to end the conversation.
"""
from app.pipeline import answer_question


def main() -> None:
    print("Chat with your documents. Type 'exit' to quit.\n")

    while True:
        question = input("You: ").strip()

        if not question:
            continue
        if question.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        try:
            result = answer_question(question)
        except Exception as e:
            print(f"[error] Something went wrong: {e}\n"
                  f"Did you run 'poetry run python -m app.ingest' first?\n")
            continue

        print(f"\nBot: {result['answer']}\n")

        sources = sorted({c["source"] for c in result["chunks"]})
        if sources:
            print(f"(sources: {', '.join(sources)})\n")


if __name__ == "__main__":
    main()
