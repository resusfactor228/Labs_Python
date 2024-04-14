line = str(input())
sort_line_letter = [a for a in line if a.isalpha()] if len([a for a in line if a.isalpha()]) else print("INPUT LINE "
                                                                                                        "IS A NUMBER")
if len([a for a in sort_line_letter if a.isupper()]) == len(sort_line_letter):
    print("YES")
else:
    print("NO")
