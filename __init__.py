# By Jerry Davos & Daxton Caylor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to
# deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
@author: Daxton Caylor & Jerry Davos
@title: ComfyUI-YouTubeVideoPlayer
@nickname: ComfyUI-YouTubeVideoPlayer
@description: YouTube Video Player in Comfy.
"""

from .classes.YouTubeVideoPlayer import N_CLASS_MAPPINGS as YouTubeVideoPlayerMappings, N_DISPLAY_NAME_MAPPINGS as YouTubeVideoPlayerNameMappings

NODE_CLASS_MAPPINGS = {}
NODE_CLASS_MAPPINGS.update(YouTubeVideoPlayerMappings)

NODE_DISPLAY_NAME_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS.update(YouTubeVideoPlayerNameMappings)

WEB_DIRECTORY = "./web"