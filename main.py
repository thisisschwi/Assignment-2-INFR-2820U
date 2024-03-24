# 100878918
# Kelvin Wong
import winsound

garray = []

def merge_sort(garray):
    print(f'sort: {garray}')
    if len(garray) > 1:
        mid = len(garray) // 2
        left_half = garray[:mid]
        right_half = garray[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                garray[k] = left_half[i]
                i += 1
            else:
                garray[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            garray[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            garray[k] = right_half[j]
            j += 1
            k += 1
        print(f'merging: {garray}')
        winsound.PlaySound('snare-112754.wav', winsound.SND_FILENAME)

def main():
    while True:
        tempint = input('Enter integer to put into array or stop to stop: ')
        if tempint.isdigit():
            tempint = int(tempint)
            garray.append(tempint)
            print(garray)
        elif tempint == 'stop':
            break
        else:
            print('Try again')
    print("Original array:", garray)
    merge_sort(garray)
    print("Sorted array:", garray)

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")