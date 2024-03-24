# 100878918
# Kelvin Wong
import winsound

garray = []  # Initialize an empty list to store integers


def merge_sort(garray):
    print(f'sort: {garray}')  # Print the current state of the array being sorted
    if len(garray) > 1:
        mid = len(garray) // 2  # Find the middle index
        # Divide the array into left half and right half
        left_half = garray[:mid]
        right_half = garray[mid:]

        # Recursively call merge_sort on left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0  # Initialize variables for left, right, and merged arrays

        # Merge the sorted left and right halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                garray[k] = left_half[i]
                i += 1
            else:
                garray[k] = right_half[j]
                j += 1
            k += 1

        # Merge any remaining elements in left half
        while i < len(left_half):
            garray[k] = left_half[i]
            i += 1
            k += 1

        # Merge any remaining elements in right half
        while j < len(right_half):
            garray[k] = right_half[j]
            j += 1
            k += 1
        print(f'merging: {garray}')  # Print the merged array
        winsound.PlaySound('snare-112754.wav', winsound.SND_FILENAME)  # Play sound



def main():
    while True:
        tempint = input('Enter integer to put into array or stop to stop: ')
        if tempint.isdigit():  # If input is a digit, add it to the array
            tempint = int(tempint)
            garray.append(tempint)
            print(garray)  # Print the current state of the array
        elif tempint == 'stop':  # If input is 'stop', exit the loop
            break
        else:  # If input is invalid, prompt the user to try again
            print('Try again')
    print("Original array:", garray)  # Print the original array
    merge_sort(garray)  # Call the merge_sort function to sort the array
    print("Sorted array:", garray)  # Print the sorted array

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")