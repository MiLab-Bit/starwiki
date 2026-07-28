## 美术资产映射（满配 v2）

transform hero_cover:
    fit "cover"
    xysize (1280, 720)

transform slow_zoom:
    zoom 1.0
    linear 12.0 zoom 1.06
    repeat

transform char_right:
    ## 旧立绘位：彻底隐藏，改用对话框旁 Q 头像
    alpha 0.0
    zoom 0.01

transform char_left:
    alpha 0.0
    zoom 0.01

transform bust_slot:
    xysize (108, 108)
    fit "cover"


transform clue_center:
    xalign 0.5
    yalign 0.38
    zoom 0.55

transform watch_hud:
    xalign 0.985
    yalign 0.02
    zoom 0.22

################################################################################
## 火星背景
################################################################################

image bg mars_storm:
    "images/A1_mars_storm.png"
    hero_cover

image bg base_alarm:
    "images/A2_base_alarm.png"
    hero_cover

image bg base_in:
    "images/A2_base_alarm.png"
    hero_cover
    matrixcolor BrightnessMatrix(-0.10)

image bg ice_cave:
    "images/A3_ice_core.png"
    hero_cover

image bg mars:
    "images/A4_dawn_chute.png"
    hero_cover

image bg mars_bleak:
    "images/A6_bleak_meet.png"
    hero_cover

image bg mars_oasis:
    "images/A7_oasis_hint.png"
    hero_cover

image bg mars_storm2:
    "images/A5_storm2.png"
    hero_cover

image bg ice_glow:
    "images/A8_ice_glow.png"
    hero_cover

image bg command:
    "images/A4_dawn_chute.png"
    hero_cover
    matrixcolor TintMatrix("#8aa0b8") * BrightnessMatrix(-0.15)

image bg moon:
    "images/moon.jpg"
    hero_cover

################################################################################
## 普林斯顿 / 共用
################################################################################

image bg study:
    "images/P_study.png"
    hero_cover

image bg lab_blue:
    "images/P_lab.png"
    hero_cover

image bg space:
    "images/P_space.png"
    hero_cover

image bg today:
    "images/P_today.png"
    hero_cover

image bg dome:
    "images/P_dome_star.png"
    hero_cover

image bg twins:
    "images/P_twins.png"
    hero_cover

image bg slowlight:
    "images/P_slowlight.png"
    hero_cover

image bg bentlight:
    "images/P_bentlight.png"
    hero_cover

################################################################################
## 立绘（全身隐藏）+ Q 版头像（对话框用）
################################################################################

## 保留原 image 名，避免旧存档/脚本报错；显示为空
image xiaoai = Null()
image xiaoai_urgent = Null()
image xiaoai_warm = Null()
image xiaoai_lost = Null()
image xiaoai_aha = Null()
image xiaoai_p = Null()

image einstein = Null()
image einstein_sneer = Null()
image einstein_warm = Null()

## Q 头像
image bust ai_normal = "images/busts/ai_normal.png"
image bust ai_urgent = "images/busts/ai_urgent.png"
image bust ai_warm = "images/busts/ai_warm.png"
image bust ai_p = "images/busts/ai_p.png"
image bust ai_lost = "images/busts/ai_lost.png"
image bust ai_aha = "images/busts/ai_aha.png"
image bust ein_normal = "images/busts/ein_normal.png"
image bust ein_sneer = "images/busts/ein_sneer.png"
image bust ein_warm = "images/busts/ein_warm.png"

default ai_bust = "normal"
default ein_bust = "normal"

init python:
    def set_ai(mood="normal"):
        store.ai_bust = mood

    def set_ein(mood="normal"):
        store.ein_bust = mood

    def bust_for_who(who):
        if who is None:
            return None
        w = str(who)
        if "小艾" in w:
            mapping = {
                "normal": "bust ai_normal",
                "urgent": "bust ai_urgent",
                "warm": "bust ai_warm",
                "p": "bust ai_p",
                "lost": "bust ai_lost",
                "aha": "bust ai_aha",
            }
            return mapping.get(store.ai_bust, "bust ai_normal")
        if ("阿尔伯特" in w) or ("爱因斯坦" in w):
            mapping = {
                "normal": "bust ein_normal",
                "sneer": "bust ein_sneer",
                "warm": "bust ein_warm",
            }
            return mapping.get(store.ein_bust, "bust ein_normal")
        return None


image prop_note = "images/D1_note.png"
image prop_rt7 = "images/D2_rt7.png"
image prop_photo = "images/D3_photo_back.png"
image prop_letter = "images/P_letter.png"
image prop_watch = "images/P_watch.png"
