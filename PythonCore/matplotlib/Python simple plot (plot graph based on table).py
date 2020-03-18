import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #path = r'C:\Users\**\learning\data\Advertising.csv'
    path = r'E:\Python\PycharmProjects\PythonCore\matplotlib\Advertising.csv'
    data = pd.read_csv(path)
    x = data[["TV", "radio", "newspaper"]]
    y = data["sales"]

    print(type(x))
    # <class 'pandas.core.frame.DataFrame'>

    print(x.shape)
    # (200, 3)

    plt.figure(figsize=(9, 12))
    plt.subplot(311)
    plt.plot(data['TV'], y, 'ro')
    plt.title('TV')
    plt.grid()

    plt.subplot(312)
    plt.plot(data['radio'], y, 'g^')
    plt.title('radio')
    plt.grid()

    plt.subplot(313)
    plt.plot(data['newspaper'], y, 'b*')
    plt.title('newspaper')
    plt.grid()

    plt.tight_layout()
    plt.show()
