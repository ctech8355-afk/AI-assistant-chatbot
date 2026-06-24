from retriever import retrieve
from generator import generate_answer
from escalation import should_escalate


print("QTrade Support Assistant")
print("Type 'exit' to quit")


while True:

    query = input("\nCustomer: ")

    if query.lower() == "exit":
        break

    if should_escalate(query):

        print("\nAssistant:")
        print(
            "This issue should be escalated "
            "to a human support agent."
        )
        continue

    docs = retrieve(query)

    answer = generate_answer(
        query,
        docs
    )

    print("\nAssistant:")
    print(answer)