

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python pipeline.py [preprocess | train | predict]")
        return

    command = sys.argv[1]

    if command == "preprocess":
        from module1.pre_processing.run_preprocessing import main as run
        run()

    # elif command == "train":
    #     from module2.train import main as run
    #     run(

    # elif command == "predict":
    #     from module3.predict import main as run
    #     run()

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()