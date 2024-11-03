def main():
    result_list = []
    list_of_dict = []

    n = int(input())
    for _ in range(n):
        start, end, cost = input().split(' ')
        list_of_dict.append(
            {
                "start": int(start),
                "end": int(end),
                "cost": int(cost),
            }
        )

    sorted_data_for_one = sorted(list_of_dict, key=lambda d: (d["start"]))
    sorted_data_for_two = sorted(list_of_dict, key=lambda d: (d["end"]))

    edge = len(sorted_data_for_one) // 2
    q = int(input())
    for _ in range(q):
        start, end, t_type = map(int, input().split(' '))

        flag_l = True
        flag_r = False
        i = edge
        if edge + 1 <= len(sorted_data_for_one) - 1:
            k = edge + 1
            flag_r = True

        if t_type == 1:
            total_cost = 0

            while flag_l or flag_r:
                if flag_l:
                    if start <= sorted_data_for_one[i]["start"] <= end:
                        total_cost += sorted_data_for_one[i]["cost"]
                    if i >= 1:
                        i -= 1
                    else:
                        flag_l = False

                if flag_r:
                    if start <= sorted_data_for_one[k]["start"] <= end:
                        total_cost += sorted_data_for_one[k]["cost"]

                    if k <= len(sorted_data_for_one) - 2:
                        k +=1
                    else:
                        flag_r = False

            result_list.append(str(total_cost))
        else:
            total_time = 0

            while flag_l or flag_r:
                if flag_l:
                    if start <= sorted_data_for_two[i]["end"] <= end:
                        total_time += sorted_data_for_two[i]["end"] - sorted_data_for_two[i]["start"]
                    if i >= 1:
                        i -= 1
                    else:
                        flag_l = False

                if flag_r:
                    if start <= sorted_data_for_two[k]["end"] <= end:
                        total_time += sorted_data_for_two[k]["end"] - sorted_data_for_two[k]["start"]
                    if k <= len(sorted_data_for_two) - 2:
                        k += 1
                    else:
                        flag_r = False

            result_list.append(str(total_time))

    print(" ".join(result_list))


if __name__ == '__main__':
    main()
