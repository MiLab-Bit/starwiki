## 天文馆 XR 剧情 Demo · 主入口
## 双剧情：《航向火星·救援队归来》（线A）×《回到普林斯顿》第1集
## 对应文档：火星多故事线_剧情与关卡设计.md / 科普剧_回到普林斯顿_第1集_20镜分镜.md

################################################################################
## 角色定义
################################################################################

define ai   = Character("小艾", color="#9ad7ff", what_color="#e8eef5")
define ein  = Character("阿尔伯特", color="#e6c88a", what_color="#f2ebe0")
define cmd  = Character("曙光号", color="#9fe6a0")
define bcast  = Character("基地广播", color="#ff9a9a", what_italic=True)
define me   = Character("[player_name]", color="#ffffff")

default player_name = "科考员"

################################################################################
## 背景 / 立绘见 images_defs.rpy
################################################################################

################################################################################
## 剧情入口（体验中枢）
################################################################################

label start:

    scene bg space with dissolve
    $ play_bgm(audio.menu_bgm)

    "欢迎回来。两条体验线各自约 15–20 分钟——请慢慢读，别快进。"

    $ player_name = renpy.input("请输入你的名字（直接回车默认为「科考员」）：", length=12).strip() or "科考员"

label demo_hub:

    scene bg space with dissolve
    $ play_bgm(audio.menu_bgm)
    call screen story_select
    $ _choice = _return

    if _choice == "mars":
        jump mars_start
    elif _choice == "princeton":
        jump princeton_start
    elif _choice == "theme":
        call screen theme_lyrics
        jump demo_hub
    else:
        jump demo_hub

################################################################################
## 通用收尾：星图成就结算
################################################################################

label epilogue_star(line_name):
    scene bg dome with dissolve
    $ play_theme(fade=2.5, loop=True)
    "天文馆穹顶亮起，你的专属星图缓缓展开。"
    "远处传来馆歌《星河有归》——The Road Home。"
    if badge_doubter:
        ai "成就入账：徽章「时间的怀疑者」"
    if star_name:
        ai "你的命名星「[star_name]」已点亮，永久保存在星图中。每次回馆，它都在。"
    ai "本次体验线：[line_name]。星图与火星线、科普剧线、AR 导览线共享账户——集齐全部剧情线，解锁隐藏展项。"
    return

label demo_end:
    call screen end_select
    if _return == "hub":
        jump demo_hub
    elif _return == "theme":
        call screen theme_lyrics
        jump demo_end
    "感谢体验。天文馆 XR 之旅，下次再会。"
    $ play_theme(fade=1.0, loop=True)
    return
