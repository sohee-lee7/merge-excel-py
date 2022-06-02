import re

# dataArray: 변경할 이차원배열
# targetHeader: 변경할 헤더의 이름
# regex: 없앨 문자열 추출할 정규식
def format_data_array(data_array, target_header, regex):
    header = data_array[0]
    data = data_array[1:]

    # 특정 컬럼 포멧팅을 위해 컬럼 index 찾기
    col_index = header.index(target_header)

    # 각 데이터에서 해당 컬럼 값 변경
    row_index = 0
    for row in data:
      # 문자열 변경
      format_str = re.sub(regex, '', row[col_index])
      # 데이터에 수정
      data[row_index][col_index] = format_str
      # 다음줄 접근을 위해 index + 1
      row_index += 1

    return [header] + data