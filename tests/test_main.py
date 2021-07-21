from app.main import delete_file

def test_delete_file(mocker):
    mocker.patch('os.path.isfile', return_value=False)
    message = delete_file('test_file_path')
    assert message == 'ファイルが存在しません。'