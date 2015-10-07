def main():
    number_of_reports = 0
    total_report_length = 0
    with open('input.txt', 'r') as fp:
    
        for line in fp:
            if 'TASK_ID=' in line:
                number_of_reports += 1                
                while '-----' not in line:
                    total_report_length += len(line)
                    line = next(fp)
    print(total_report_length/number_of_reports)

if __name__ == '__main__':
    main()