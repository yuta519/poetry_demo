import os


# テスト対象のメソッド
def delete_file(file_path):
    try:
        if not os.path.isfile(file_path):
            return 'ファイルが存在しません。'
        
        os.remove(file_path)

        return 'ファイルを削除しました。'
    except:
        return 'エラーが発生しました。'


def test_delete_file(mocker):
    mocker.patch('os.path.isfile', return_value=False)
    message = delete_file('test_file_path')
    assert message == 'ファイルが存在しません。'
