import sys
import scale_explorer

if __name__ == "__main__":
    print("hello world")
    if len(sys.argv) > 1 and sys.argv[1] == "scale_explorer":
        print(sys.argv[1])
        scale_explorer.run()
    print(sys.argv)