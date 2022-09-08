import csv
import sys
import os
import cairosvg


csv_file_path = sys.argv[1]
svg_long_file_path = sys.argv[2]
svg_short_file_path = sys.argv[3]
output_folder = sys.argv[4]

if not output_folder.endswith('/'):
    output_folder += '/'



with open(csv_file_path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    cnt = 0
    for row in reader:
        if cnt != 0:
            if 'Virtual Attendance' != row[12]:
                print((row[2], row[3], row[5], row[12]))
                if not os.path.exists(output_folder + 'svg'):
                    os.mkdir(output_folder + 'svg')
                    os.mkdir(output_folder + 'png')
                output_file = open(output_folder + 'svg/badge' + str(cnt) + '.svg', 'w', encoding='utf-8')
                full_name = row[3] + ' ' + row[2]
                if len(full_name) < 15:
                    svg = open(svg_short_file_path, 'r', encoding='utf-8')
                    for line in svg:
                        output_file.write(line.replace('attendant_name', full_name).replace('organization_name', row[5]))
                    output_file.close()
                    svg.close()
                else:
                    svg = open(svg_long_file_path, 'r', encoding='utf-8')
                    for line in svg:
                        output_file.write(line.replace('first_name', row[3]).replace('last_name', row[2]).replace('organization_name', row[5]))
                    output_file.close()
                    svg.close()
                
                cairosvg.svg2png(url=output_folder + 'svg/badge' + str(cnt) + '.svg', write_to=output_folder + 'png/badge' + str(cnt) + '.png', dpi=300)

        cnt += 1
