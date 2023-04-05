from queue import Queue


if __name__ == "__main__":
    queue = Queue(6)

    for i in range(2,9):
        queue.display_status()
        try:
            queue.enqueue(i)
        except Exception as e:
            print(e)

    queue.display_status()

    for i in range(6):
        try:
            dequeued_data = queue.dequeue()
            queue.display_status()
            print(f"取り出したデータ {dequeued_data}")
        except Exception as e:
            print(e)
