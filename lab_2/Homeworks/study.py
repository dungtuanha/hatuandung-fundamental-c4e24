from youtube_dl import YoutubeDL

dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])

#______________________________________________________________________

dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])

#_______________________________________________________________________

options = {
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])

#__________________________________________________________________________

options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1
}
dl = YoutubeDL(options)
dl.download(['con điên TAMKA PKL'])

#_____________________________________________________________________________

options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1, 
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Chờ anh nhé Hoàng Dũng'])