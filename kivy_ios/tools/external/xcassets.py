"""
Icon and LaunchImage generator for iOS
======================================

.. author:: Mathieu Virbel <mat@meltingrocks.com>
"""
# flake8: noqa (E121 mainly)

__all__ = ["launchimage"]

import sh
import json
from PIL import Image
from os.path import join, exists
from os import makedirs

appicon_json = {
  "images" : [
    {
      "filename" : "Icon40.png",
      "idiom" : "iphone",
      "scale" : "2x",
      "size" : "20x20"
    },
    {
      "filename" : "Icon60.png",
      "idiom" : "iphone",
      "scale" : "3x",
      "size" : "20x20"
    },
    {
      "filename" : "Icon29.png",
      "idiom" : "iphone",
      "scale" : "1x",
      "size" : "29x29"
    },
    {
      "filename" : "Icon58.png",
      "idiom" : "iphone",
      "scale" : "2x",
      "size" : "29x29"
    },
    {
      "filename" : "Icon87.png",
      "idiom" : "iphone",
      "scale" : "3x",
      "size" : "29x29"
    },
    {
      "filename" : "Icon80.png",
      "idiom" : "iphone",
      "scale" : "2x",
      "size" : "40x40"
    },
    {
      "filename" : "Icon120.png",
      "idiom" : "iphone",
      "scale" : "3x",
      "size" : "40x40"
    },
    {
      "filename" : "Icon57.png",
      "idiom" : "iphone",
      "scale" : "1x",
      "size" : "57x57"
    },
    {
      "filename" : "Icon114.png",
      "idiom" : "iphone",
      "scale" : "2x",
      "size" : "57x57"
    },
    {
      "filename" : "Icon120.png",
      "idiom" : "iphone",
      "scale" : "2x",
      "size" : "60x60"
    },
    {
      "filename" : "Icon180.png",
      "idiom" : "iphone",
      "scale" : "3x",
      "size" : "60x60"
    },
    {
      "filename" : "Icon20.png",
      "idiom" : "ipad",
      "scale" : "1x",
      "size" : "20x20"
    },
    {
      "filename" : "Icon40.png",
      "idiom" : "ipad",
      "scale" : "2x",
      "size" : "20x20"
    },
    {
      "filename" : "Icon29.png",
      "idiom" : "ipad",
      "scale" : "1x",
      "size" : "29x29"
    },
    {
      "filename" : "Icon58.png",
      "idiom" : "ipad",
      "scale" : "2x",
      "size" : "29x29"
    },
    {
      "filename" : "Icon40.png",
      "idiom" : "ipad",
      "scale" : "1x",
      "size" : "40x40"
    },
    {
      "filename" : "Icon80.png",
      "idiom" : "ipad",
      "scale" : "2x",
      "size" : "40x40"
    },
    {
      "filename" : "Icon50.png",
      "idiom" : "ipad",
      "scale" : "1x",
      "size" : "50x50"
    },
    {
      "filename" : "Icon100.png",
      "idiom" : "ipad",
      "scale" : "2x",
      "size" : "50x50"
    },
    {
      "filename" : "Icon72.png",
      "idiom" : "ipad",
      "scale" : "1x",
      "size" : "72x72"
    },
    {
      "filename" : "Icon144.png",
      "idiom" : "ipad",
      "scale" : "2x",
      "size" : "72x72"
    },
    {
      "filename" : "Icon76.png",
      "idiom" : "ipad",
      "scale" : "1x",
      "size" : "76x76"
    },
    {
      "filename" : "Icon152.png",
      "idiom" : "ipad",
      "scale" : "2x",
      "size" : "76x76"
    },
    {
      "filename" : "Icon167.png",
      "idiom" : "ipad",
      "scale" : "2x",
      "size" : "83.5x83.5"
    },
    {
      "filename" : "Icon1024.png",
      "idiom" : "ios-marketing",
      "scale" : "1x",
      "size" : "1024x1024"
    },
    {
      "filename" : "Icon48.png",
      "idiom" : "watch",
      "role" : "notificationCenter",
      "scale" : "2x",
      "size" : "24x24",
      "subtype" : "38mm"
    },
    {
      "filename" : "Icon55.png",
      "idiom" : "watch",
      "role" : "notificationCenter",
      "scale" : "2x",
      "size" : "27.5x27.5",
      "subtype" : "42mm"
    },
    {
      "filename" : "Icon58.png",
      "idiom" : "watch",
      "role" : "companionSettings",
      "scale" : "2x",
      "size" : "29x29"
    },
    {
      "filename" : "Icon87.png",
      "idiom" : "watch",
      "role" : "companionSettings",
      "scale" : "3x",
      "size" : "29x29"
    },
    {
      "idiom" : "watch",
      "role" : "notificationCenter",
      "scale" : "2x",
      "size" : "33x33",
      "subtype" : "45mm"
    },
    {
      "filename" : "Icon80.png",
      "idiom" : "watch",
      "role" : "appLauncher",
      "scale" : "2x",
      "size" : "40x40",
      "subtype" : "38mm"
    },
    {
      "filename" : "Icon88.png",
      "idiom" : "watch",
      "role" : "appLauncher",
      "scale" : "2x",
      "size" : "44x44",
      "subtype" : "40mm"
    },
    {
      "idiom" : "watch",
      "role" : "appLauncher",
      "scale" : "2x",
      "size" : "46x46",
      "subtype" : "41mm"
    },
    {
      "filename" : "Icon100.png",
      "idiom" : "watch",
      "role" : "appLauncher",
      "scale" : "2x",
      "size" : "50x50",
      "subtype" : "44mm"
    },
    {
      "idiom" : "watch",
      "role" : "appLauncher",
      "scale" : "2x",
      "size" : "51x51",
      "subtype" : "45mm"
    },
    {
      "filename" : "Icon172.png",
      "idiom" : "watch",
      "role" : "quickLook",
      "scale" : "2x",
      "size" : "86x86",
      "subtype" : "38mm"
    },
    {
      "filename" : "Icon196.png",
      "idiom" : "watch",
      "role" : "quickLook",
      "scale" : "2x",
      "size" : "98x98",
      "subtype" : "42mm"
    },
    {
      "filename" : "Icon216.png",
      "idiom" : "watch",
      "role" : "quickLook",
      "scale" : "2x",
      "size" : "108x108",
      "subtype" : "44mm"
    },
    {
      "idiom" : "watch",
      "role" : "quickLook",
      "scale" : "2x",
      "size" : "117x117",
      "subtype" : "45mm"
    },
    {
      "filename" : "Icon1024.png",
      "idiom" : "watch-marketing",
      "scale" : "1x",
      "size" : "1024x1024"
    },
    {
      "filename" : "Icon16.png",
      "idiom" : "mac",
      "scale" : "1x",
      "size" : "16x16"
    },
    {
      "filename" : "Icon32.png",
      "idiom" : "mac",
      "scale" : "2x",
      "size" : "16x16"
    },
    {
      "filename" : "Icon32.png",
      "idiom" : "mac",
      "scale" : "1x",
      "size" : "32x32"
    },
    {
      "filename" : "Icon64.png",
      "idiom" : "mac",
      "scale" : "2x",
      "size" : "32x32"
    },
    {
      "filename" : "Icon128.png",
      "idiom" : "mac",
      "scale" : "1x",
      "size" : "128x128"
    },
    {
      "filename" : "Icon256.png",
      "idiom" : "mac",
      "scale" : "2x",
      "size" : "128x128"
    },
    {
      "filename" : "Icon256.png",
      "idiom" : "mac",
      "scale" : "1x",
      "size" : "256x256"
    },
    {
      "filename" : "Icon512.png",
      "idiom" : "mac",
      "scale" : "2x",
      "size" : "256x256"
    },
    {
      "filename" : "Icon512.png",
      "idiom" : "mac",
      "scale" : "1x",
      "size" : "512x512"
    },
    {
      "filename" : "Icon1024.png",
      "idiom" : "mac",
      "scale" : "2x",
      "size" : "512x512"
    },
    {
      "filename" : "Icon88.png",
      "idiom" : "watch",
      "role" : "longLook",
      "scale" : "2x",
      "size" : "44x44",
      "subtype" : "42mm"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}



launchimage_json = {
  "images": [
    {
      "extent": "full-screen",
      "idiom": "iphone",
      "subtype": "736h",
      "filename": "Default1242x2208.png",
      "minimum-system-version": "8.0",
      "orientation": "portrait",
      "scale": "3x"
    },
    {
      "extent": "full-screen",
      "idiom": "iphone",
      "subtype": "736h",
      "filename": "Default2208x1242.png",
      "minimum-system-version": "8.0",
      "orientation": "landscape",
      "scale": "3x"
    },
    {
      "extent": "full-screen",
      "idiom": "iphone",
      "subtype": "667h",
      "filename": "Default750x1334.png",
      "minimum-system-version": "8.0",
      "orientation": "portrait",
      "scale": "2x"
    },
    {
      "orientation": "portrait",
      "idiom": "iphone",
      "extent": "full-screen",
      "minimum-system-version": "7.0",
      "filename": "Default640x960.png",
      "scale": "2x"
    },
    {
      "extent": "full-screen",
      "idiom": "iphone",
      "subtype": "retina4",
      "filename": "Default640x1136.png",
      "minimum-system-version": "7.0",
      "orientation": "portrait",
      "scale": "2x"
    },
    {
      "orientation": "portrait",
      "idiom": "ipad",
      "extent": "full-screen",
      "minimum-system-version": "7.0",
      "filename": "Default768x1024.png",
      "scale": "1x"
    },
    {
      "orientation": "landscape",
      "idiom": "ipad",
      "extent": "full-screen",
      "minimum-system-version": "7.0",
      "filename": "Default1024x768.png",
      "scale": "1x"
    },
    {
      "orientation": "portrait",
      "idiom": "ipad",
      "extent": "full-screen",
      "minimum-system-version": "7.0",
      "filename": "Default1536x2048.png",
      "scale": "2x"
    },
    {
      "orientation": "landscape",
      "idiom": "ipad",
      "extent": "full-screen",
      "minimum-system-version": "7.0",
      "filename": "Default2048x1536.png",
      "scale": "2x"
    },
    {
      "orientation": "portrait",
      "idiom": "iphone",
      "extent": "full-screen",
      "filename": "Default320x480.png",
      "scale": "1x"
    },
    {
      "orientation": "portrait",
      "idiom": "iphone",
      "extent": "full-screen",
      "filename": "Default640x960.png",
      "scale": "2x"
    },
    {
      "orientation": "portrait",
      "idiom": "iphone",
      "extent": "full-screen",
      "filename": "Default640x1136.png",
      "subtype": "retina4",
      "scale": "2x"
    },
    {
      "orientation": "portrait",
      "idiom": "ipad",
      "extent": "full-screen",
      "filename": "Default768x1024.png",
      "scale": "1x"
    },
    {
      "orientation": "landscape",
      "idiom": "ipad",
      "extent": "full-screen",
      "filename": "Default1024x768.png",
      "scale": "1x"
    },
    {
      "orientation": "portrait",
      "idiom": "ipad",
      "extent": "full-screen",
      "filename": "Default1536x2048.png",
      "scale": "2x"
    },
    {
      "orientation": "landscape",
      "idiom": "ipad",
      "extent": "full-screen",
      "filename": "Default2048x1536.png",
      "scale": "2x"
    },
  ],
  "info": {
    "version": 1,
    "author": "xcode"
  }
}


def icon(image_xcassets, image_fn):
    """Generate all the possible Icon from a single image_fn
    """
    appicon_dir = join(image_xcassets, "AppIcon.appiconset")
    if not exists(appicon_dir):
        makedirs(appicon_dir)
    with open(join(appicon_dir, "Contents.json"), "w") as fd:
        json.dump(appicon_json, fd)

    options = (
        # iPhone
        # Spotlight - iOS 5,6
        # Settings - iOS 5-8
        # 29pt - 1x,2x,3x
        ("87", None, "Icon87.png"),
        ("58", None, "Icon58.png"),
        ("29", "Icon58.png", "Icon29.png"),

        # iPhone notification
        # 20pt - 2x,3x
        # ("40", None, "Icon40.png"),
        ("60", None, "Icon60.png"),

        # iPhone
        # Spotlight - iOS 7-8
        # 40pt 2x,3x
        ("120", None, "Icon120.png"),
        ("80", None, "Icon80.png"),

        # iPhone
        # App - iOS 5,6
        # 57pt 1x,2x
        ("114", None, "Icon114.png"),
        ("57", "Icon114.png", "Icon57.png"),

        # iPhone
        # App - iOS 7,8
        # 60pt 2x,3x
        ("180", None, "Icon180.png"),
        # ("120", None, "Icon120.png # duplicate"),

        # iPad
        # Notifications
        # 20pt 1x,2x
        ("20", "Icon80.png", "Icon20.png"),
        ("40", "Icon80.png", "Icon40.png"),

        # iPad
        # Settings iOS 5-8
        # ("58", None, "Icon58.png # duplicate"),
        # ("29", "Icon58.png", "Icon29.png # duplicate"),

        # iPad
        # Spotlight iOS 7,8
        # 40pt 1x,2x
        # ("80", None, "Icon80.png # duplicate"),
        ("40", "Icon80.png", "Icon40.png"),

        # iPad
        # Spotlight iOS 5,6
        # 50pt 1x,2x
        ("100", None, "Icon100.png"),
        ("50", "Icon100.png", "Icon50.png"),

        # iPad
        # App iOS 5,6
        # 72pt 1x,2x
        ("144", None, "Icon144.png"),
        ("72", "Icon144.png", "Icon72.png"),

        # iPad
        # App iOS 7,8
        # 76pt 1x,2x
        ("152", None, "Icon152.png"),
        ("76", "Icon152.png", "Icon76.png"),

        # iPad
        # App iOS 9
        # 83.5pt 2x
        ("167", None, "Icon167.png"),


        # CarPlay
        # App iOS 8
        # 120pt 1x
        # ("120", None, "Icon120.png # duplicate"),


        # Apple Watch
        # Notification Center
        # 38mm, 42mm
        ("48", None, "Icon48.png"),
        ("55", None, "Icon55.png"),

        # Apple Watch
        # Companion Settings
        # 29pt 2x,3x
        # ("58", None, "Icon58.png # duplicate"),
        # ("87", None, "Icon87.png # duplicate"),

        # Apple Watch
        # Home Screen (All)
        # Long Look (38mm)
        # ("80", None, "Icon80.png # duplicate"),

        # Apple Watch
        # Long Look (42mm)
        ("88", None, "Icon88.png"),

        # Apple Watch
        # Short Look
        # 38mm, 42mm, 44mm
        ("172", None, "Icon172.png"),
        ("196", None, "Icon196.png"),
        ("216", None, "Icon216.png"),


        # OS X
        # 512pt 1x,2x
        ("1024", None, "Icon1024.png"),
        ("512", "Icon1024.png", "Icon512.png"),

        # OS X
        # 256pt 1x,2x
        # ("512", "Icon1024.png", "Icon512.png # duplicate"),
        ("256", "Icon512.png", "Icon256.png"),

        # OS X
        # 128pt 1x,2x
        # ("256", "Icon512.png", "Icon256.png # duplicate"),
        ("128", "Icon256.png", "Icon128.png"),

        # OS X
        # 32pt 1x,2x
        ("64", "Icon128.png", "Icon64.png"),
        ("32", "Icon64.png", "Icon32.png"),

        # OS X
        # 16pt 1x,2x
        # ("32", "Icon64.png", "Icon32.png # duplicate"),
        ("16", "Icon32.png", "Icon16.png"))

    _generate("AppIcon.appiconset", image_xcassets, image_fn, options, icon=True)


def launchimage(image_xcassets, image_fn):
    """Generate all the possible Launch Images from a single image_fn
    """
    launchimage_dir = join(image_xcassets, "LaunchImage.launchimage")
    if not exists(launchimage_dir):
        makedirs(launchimage_dir)
    with open(join(launchimage_dir, "Contents.json"), "w") as fd:
        json.dump(launchimage_json, fd)

    options = (
        # size, input, output
        # iPhone 3.5" @2x
        ("640 960", None, "Default640x960.png"),
        # iPhone 3.5" @1x
        ("320 480", None, "Default320x480.png"),
        # iPhone 4.0" @2x
        ("640 1136", None, "Default640x1136.png"),
        # iPhone 5.5" @3x - landscape
        ("2208 1242", None, "Default2208x1242.png"),
        # iPhone 5.5" @3x - portrait
        ("1242 2208", None, "Default1242x2208.png"),
        # iPhone 4.7" @2x
        ("750 1334", None, "Default750x1334.png"),
        # iPad @2x - landscape
        ("2048 1536", None, "Default2048x1536.png"),
        # iPad @2x - portrait
        ("1536 2048", None, "Default1536x2048.png"),
        # iPad @1x - landscape
        ("1024 768", None, "Default1024x768.png"),
        # iPad @1x - portrait
        ("768 1024", None, "Default768x1024.png"),
    )

    _generate("LaunchImage.launchimage", image_xcassets, image_fn, options)


def _buildimage(in_fn, out_fn, size, padcolor=None):
    im = Image.open(in_fn)

    # read the first left/bottom pixel
    bgcolor = im.getpixel((0, 0))

    # ensure the image fit in the destination size
    if im.size[0] > size[0] or im.size[1] > size[1]:
        f = max(im.size[0] / size[0], im.size[1] / size[1])
        newsize = int(im.size[0] / f), int(im.size[1] / f)
        im = im.resize(newsize)

    # create final image
    outim = Image.new("RGB", size, bgcolor[:3])
    x = (size[0] - im.size[0]) // 2
    y = (size[1] - im.size[1]) // 2
    outim.paste(im, (x, y))

    # save the image
    outim.save(out_fn)


def _generate(d, image_xcassets, image_fn, options, icon=False):
    for c, in_fn, out_fn in options:
        args = []
        if in_fn is not None:
            filename = join(image_xcassets, d, in_fn)
        else:
            filename = image_fn

        if icon:
            args += [filename, "-Z", c]
            args += [
                "--out",
                join(image_xcassets, d, out_fn)
            ]
            print("sips", " ".join(args))
            sh.sips(*args)

        size = [int(x) for x in c.split()]
        _buildimage(filename, join(image_xcassets, d, out_fn), size)
