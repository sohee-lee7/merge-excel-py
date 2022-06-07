## pyinstaller

```shell
$ pyinstaller -w -F gui.py
```

### with pyexcel

```shell
$ pyinstaller -w -F gui.py --hidden-import pyexcel_io.readers.csv_in_file --hidden-import pyexcel_io.readers.csv_in_memory --hidden-import pyexcel_io.readers.csv_content --hidden-import pyexcel_io.readers.csvz --hidden-import pyexcel_io.writers.csv_in_file --hidden-import pyexcel_io.writers.csv_in_memory --hidden-import pyexcel_io.writers.csvz_writer --hidden-import pyexcel_io.database.importers.django --hidden-import pyexcel_io.database.importers.sqlalchemy --hidden-import pyexcel_io.database.exporters.django --hidden-import pyexcel_io.database.exporters.sqlalchemy --hidden-import pyexcel_xlsx --hidden-import pyexcel_xlsx.xlsxr --hidden-import pyexcel_xlsx.xlsxw --hidden-import pyexcel_xls --hidden-import pyexcel_xls.xlsr --hidden-import pyexcel_xls.xlsw --hidden-import pyexcel_xlsxw --hidden-import pyexcel_xlsxw.xlsxw
```