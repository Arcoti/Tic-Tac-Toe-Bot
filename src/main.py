from model.train import train
import matplotlib.pyplot as plt

def main():
    winRate, drawRate, lossRate = train(1)

    x = [i * 1000 for i in range(1, len(winRate) + 1)]
    plt.plot(x, winRate, label="Win Rate")
    plt.plot(x, drawRate, label="Draw Rate")
    plt.plot(x, lossRate, label="Loss Rate")
    plt.xlabel("Episodes")
    plt.ylabel("Rate")
    plt.title("Learning Curse of Q Learning Algorithm")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()