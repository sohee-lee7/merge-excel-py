import os
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
    book = px.get_book(file_name=file_dir)

    # file 각 시트 데이터 가져오기
    for sheetname in book.sheet_names():
      sheet = px.get_sheet(file_name=file_dir, sheet_name=sheetname)
      origin_data = sheet.get_array()

      format_data = format_data_array(origin_data, target_header, regex)

      # 시트별로 데이터를 분류하기 위해 directory 형태로 저장
      if sheetname in result:
        # 이미 directory에 있는 sheet면 헤더 제외하고 data 합치기
        result[sheetname] += format_data[1:]
      else:
        # directory에 없는 sheet면 헤더가 있는 전체 format_data 넣기
        result[sheetname] = format_data


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