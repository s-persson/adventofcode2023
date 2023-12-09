def main():
    time = 6717999
    distance = 334113513502430
    first_win = 0
    last_win = 0
    for x in range(time):
            if (x * (time - x)) > distance:
                first_win = x
                break
    for x in range(time, 0, -1):
          if (x * (time - x)) > distance:
                last_win = x
                break
    print(last_win - first_win)
if __name__ == "__main__":
    main()
