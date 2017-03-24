#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
    #make a list of possible fortune_sentence
    fortune = [
        "You must use the Force!",
        "I see much code in your future!",
        "Consider eating more fortune cookies",
        "Don't take the blue pill",
        "You have tamed the mighty Python, now you must free it onto the Great Spider's Web!"
    ]
    #randomly select one of the fortune


    return random.choice(fortune)
class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = '<h1>Fortune Cookie</h1>'

        fortune = '<strong>' + getRandomFortune() + '</strong>'
        fortune_sentence = "Your fortune: " + fortune
        fortune_paragraph = '<p>' + fortune_sentence + '<p>'


        lucky_number = '<strong>' + str(random.randint(1,100)) + '</strong>'
        number_sentence = 'Your lucky number: ' + lucky_number
        number_paragraph = '<p>' + number_sentence + '</p>'

        cookie_again_button = "<a href='.'><button>Another cookie plz!</button><a>"
        content = header + fortune_paragraph + number_paragraph
        self.response.write(header + fortune_paragraph + number_paragraph + cookie_again_button )



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
