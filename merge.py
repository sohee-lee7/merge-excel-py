import os
import re
import pyexcel as px

directory = '/Users/soheelee/Desktop/python-data'
filelist = os.listdir(directory)

outData = {}

for filename in filelist:
  if '.xlsx' not in filename:
    continue
  fileDir = directory + '/' + filename

  # file 읽기
  book = px.get_book(file_name=fileDir)

  # file 각 시트 데이터 가져오기
  for sheetname in book.sheet_names():
    sheet = px.get_sheet(file_name=fileDir,sheet_name=sheetname)
    originData = sheet.get_array()

    # 헤더와 데이터를 각 변수에 저장
    header = originData[0]
    data = originData[1:]

    # 특정 컬럼 포멧팅을 위해 컬럼 index 찾기
    colIndex = header.index('HEAD_C')

    # 각 데이터에서 해당 컬럼 값 변경
    rowIndex = 0
    for row in data:
      # 문자열 변경
      formatStr = re.sub('-[a-zA-Z0-9]*', '', row[colIndex])
      # 데이터에 수정
      data[rowIndex][colIndex] = formatStr
      # 다음줄 접근을 위해 index + 1
      rowIndex += 1

    # 시트별로 데이터를 분류하기 위해 directory 형태로 저장
    if sheetname in outData:
      # 이미 directory에 있는 sheet면 헤더가 없는 data 합치기
      outData[sheetname] += data
    else:
      # directory에 없는 sheet면 헤더가 있는 전체 originData 넣기
      outData[sheetname] = originData


# 합산된 시트 데이터를 하나의 파일로 만들기
for key in outData.keys():
  px.save_as(array=outData[key], dest_file_name=directory + '/' + key + '.csv', sheet_name=key)