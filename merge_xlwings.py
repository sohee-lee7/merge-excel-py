import os
import xlwings as xw
import pyexcel as px
from format import format_data_array

# directory: 폴더 위치
# target_header: 포맷팅할 헤더 이름
# regex: 포맷할 정규식
def merge_excel(directory, target_header, regex):
  filelist = os.listdir(directory)

  result = {}

  for filename in filelist:
    if '.xlsx' not in filename:
      continue
    file_dir = directory + '/' + filename

    # file 읽기
    book = xw.Book(file_dir)

    # file 각 시트 데이터 가져오기
    for sheet in book.sheets:
      sheetname = sheet.name

      # 마지막 column, row 찾기
      num_col = sheet.range('A1').end('right').column
      num_row = sheet.range('A1').end('down').row

      # 데이터 가져오기
      origin_data = sheet.range((1,1),(num_row,num_col)).value
      print(origin_data)

      if target_header and regex:
        format_data = format_data_array(origin_data, target_header, regex)
      else:
        format_data = origin_data

      # 시트별로 데이터를 분류하기 위해 directory 형태로 저장
      if sheetname in result:
        # 이미 directory에 있는 sheet면 헤더 제외하고 data 합치기
        result[sheetname] += format_data[1:]
      else:
        # directory에 없는 sheet면 헤더가 있는 전체 format_data 넣기
        result[sheetname] = format_data

      book.close()


  result_files = []

  # 합산된 시트 데이터를 하나의 파일로 만들기
  # for key in result.keys():
  #   px.save_as(array=result[key], dest_file_name=directory + '/' + key + '.csv', sheet_name=key)
  #   result_files.append(key + '.csv')

  # 합산된 시트를 지정된 이름의 파일로 만들기
  index = 0
  for key in result.keys():
    if index == 0:
      px.save_as(array=result[key], dest_file_name=directory + '/' + 'CH.csv', sheet_name=key)
      result_files.append(key + '.csv')
    elif index == 1:
      px.save_as(array=result[key], dest_file_name=directory + '/' + 'HTH.csv', sheet_name=key)
      result_files.append(key + '.csv')
    else:
      px.save_as(array=result[key], dest_file_name=directory + '/' + key + '.csv', sheet_name=key)
      result_files.append(key + '.csv')
    index += 1


  # 결과값을 생성된 파일이름으로 보내주기
  return result_files