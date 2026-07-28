## 声音设计 · 通道与便捷指令
## 主题曲：《The Road Home / 星河有归》→ audio/song_theme.mp3

init python:
    renpy.music.register_channel("ambient", mixer="music", loop=True)

## 主题曲片长约 382s；前奏后再滚歌词（可按成曲改）
define THEME_INTRO_SEC = 28.0

## 菜单 / 穹顶：挂主题曲；旧程序合成器乐仍保留作场景 BGM
define audio.menu_bgm = "audio/song_theme.mp3"
define audio.menu_bgm_legacy = "audio/bgm_menu.wav"
define audio.mars_storm = "audio/amb_mars_storm.wav"
define audio.mars_cabin = "audio/bgm_mars_cabin.wav"
define audio.mars_lost = "audio/bgm_mars_lost.wav"
define audio.mars_reunion = "audio/bgm_mars_reunion.wav"
define audio.princeton_study = "audio/bgm_princeton_study.wav"
define audio.princeton_take = "audio/bgm_princeton_take.wav"
define audio.dome = "audio/song_theme.mp3"
define audio.dome_legacy = "audio/bgm_dome.wav"
define audio.amb_cabin = "audio/amb_cabin.wav"
define audio.amb_study = "audio/amb_study.wav"
define audio.amb_today = "audio/amb_today.wav"

define audio.sfx_alarm = "audio/sfx_alarm.wav"
define audio.sfx_ok = "audio/sfx_ok.wav"
define audio.sfx_deny = "audio/sfx_deny.wav"
define audio.sfx_scan = "audio/sfx_scan.wav"
define audio.sfx_signal = "audio/sfx_signal.wav"
define audio.sfx_ice = "audio/sfx_ice_core.wav"
define audio.sfx_ether = "audio/sfx_ether_crack.wav"
define audio.sfx_tick = "audio/sfx_watch_tick.wav"
define audio.sfx_desync = "audio/sfx_watch_desync.wav"

init python:
    def audio_hush(fade=1.5):
        """关键拍抽空：停 music + ambient。"""
        renpy.music.stop(channel="music", fadeout=fade)
        renpy.music.stop(channel="ambient", fadeout=fade)

    def play_amb(track, fade=1.5):
        renpy.music.play(track, channel="ambient", loop=True, fadein=fade)

    def play_bgm(track, fade=1.5, loop=True):
        renpy.music.play(track, channel="music", loop=loop, fadein=fade)

    def play_theme(fade=2.0, loop=True):
        """馆歌《星河有归》专用入口。"""
        renpy.music.play(audio.song_theme, channel="music", loop=loop, fadein=fade)
