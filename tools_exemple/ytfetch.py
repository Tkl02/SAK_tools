from pytubefix import YouTube
from pytubefix.cli import on_progress
import sys
import os
from pathlib import Path

def help_menu():
    print("""
Objetivo: baixar vídeo ou áudio do YouTube

Qualidade:
  -l, --low       -> baixa qualidade
  -m, --middle    -> média qualidade
  -h, --high      -> alta qualidade

Tipo:
  -v, --video     -> baixar vídeo
  -a, --audio     -> baixar áudio

URL:
  -u, --url       -> URL do YouTube

Exemplos:
  ytDownload -u <url> -h -v
  ytDownload -u <url> -m -a
""")

def confirmation(yt):
	yt = yt
	confirm = input(f"Deseja baixar {yt.title}?(Y/n): ")
	if confirm in ("N", "n", "no","No"):
		print("Processo cancelado")
		return True
	return False

def download_video(url, quality):
	downloads = Path.home() / "Downloads"
	path_destiny = downloads / "youtube_of_downloads"
	path_destiny.mkdir(parents=True, exist_ok=True)
	yt = YouTube(url, on_progress_callback= on_progress)
	if confirmation(yt):
		return

	if quality == "low":
		stream = yt.streams.filter(progressive=True).order_by("resolution").first()
	elif quality == "middle":
		stream = yt.streams.filter(progressive=True).order_by("resolution")[len(yt.streams.filter(progressive=True)) // 2 ]
	else:
		stream = yt.streams.get_highest_resolution()
	
	stream.download(path_destiny)
	print("Download Concluido")


def download_music(url, quality):
	downloads = Path.home() / "Downloads"
	path_destiny = downloads / "youtube_of_downloads"
	path_destiny.mkdir(parents=True, exist_ok=True)
	yt = YouTube(url, on_progress_callback= on_progress)
	if confirmation(yt):
		return

	stream = yt.streams.filter(only_audio=True).order_by("abr").desc().first()
	out_file = stream.download(path_destiny)

	base, _ = os.path.splitext(out_file)
	new_file = base + ".mp3"
	os.rename(out_file, new_file)

	print("Download Concluido")

def main():
	args = sys.argv[1:]

	if not args or "-h" in args or "--help" in args:
		help_menu()
		return
	
	url = None
	quality = "high"
	mode = None

	i = 0
	while i < len(args):
		arg = args[i]

		if arg in ("-u", "--url"):
			url = args[i+1]
			i+=1
		elif arg in ("-l", "--low"):
			quality = "low"
		elif arg in ("-m", "--middle"):
			quality = "middle"
		elif arg in ("-h", "--high"):
			quality = "high"
		elif arg in ("-v", "--video"):
			mode = "video"
		elif arg in ("-a", "--audio"):
			mode = "audio"

		i+=1
	
	if not url or not mode:
		print("Erro: url ou modo não informado")
		help_menu()
		return
	
	if mode == "video":
		download_video(url, quality)
	if mode == "audio":
		download_music(url, quality)


if __name__ == "__main__":
	main()