# 実行したときに、自動で複数のウェブページやソフトを開く
import webbrowser # ウェブページを開く標準ライブラリ
import subprocess # ソフトを起動する標準ライブラリ
import time

def main():
    spreadsheet_url = r"GoogleSpreadsheetのURL"
    document_url = r"GoogleDocumentのURL"
    github_url = r"GitHubのURL"
    atcoder_url = r"AtCoderのURL"
    atcoderproblems_url = r"AtcoderProblemsのURL"
    gemini_url = r"GeminiのURL"
    
    urls = [spreadsheet_url, document_url, gemini_url, github_url, atcoder_url, atcoderproblems_url]
    for url in urls:
        webbrowser.open(url)
        time.sleep(0.5)

    time.sleep(2)
    # VSCodeを起動
    subprocess.Popen("code", shell=True) # shell=True: windowsシステム経由で実行


if __name__ == "__main__":
    main()