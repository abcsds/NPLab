#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4post1),
    on Fri 09 Oct 2020 02:06:21 PM CEST
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

from pylsl import StreamInfo, StreamOutlet



# Setup the LSL stream
info = StreamInfo(name='PsychoPy', type='Markers', channel_count=1,
                  channel_format='int32', source_id='AUniqueID42')
# Initialize the LSL stream.
outlet = StreamOutlet(info)



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4post1'
expName = 'main'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='main.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
Welcome_text = visual.TextStim(win=win, name='Welcome_text',
    text="Welcome!\n\nIn the next minutes you will be prompted with two tasks: First you'll watch some pictures and later a shrot video, please follow the instructions on screen. \n\nWhen you are ready, press the spacebar...",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "baseline"
baselineClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='Please look at the following pictures.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
image_01 = visual.ImageStim(
    win=win,
    name='image_01',
    image='exp_data/img/01.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_02 = visual.ImageStim(
    win=win,
    name='image_02',
    image='exp_data/img/02.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_03 = visual.ImageStim(
    win=win,
    name='image_03',
    image='exp_data/img/03.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_04 = visual.ImageStim(
    win=win,
    name='image_04',
    image='exp_data/img/04.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_05 = visual.ImageStim(
    win=win,
    name='image_05',
    image='exp_data/img/05.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_cross = visual.ShapeStim(
    win=win, name='fixation_cross', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "stimulus"
stimulusClock = core.Clock()
movie = visual.MovieStim3(
    win=win, name='movie',
    noAudio = False,
    filename='./exp_data/Dragon.mp4',
    ori=0, pos=(0, 0), opacity=1,
    loop=False,
    depth=0.0,
    )

# Initialize components for Routine "Scale"
ScaleClock = core.Clock()
scale_text = visual.TextStim(win=win, name='scale_text',
    text='Lastly, we present you two scales: arousal (excitement) and valence. Please rate how the video made you feel. When you are done, press the spacebar.',
    font='Arial',
    pos=(0, .3), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
scale_a = visual.ImageStim(
    win=win,
    name='scale_a',
    image='exp_data/img/SAM-A-9.png', mask=None,
    ori=0, pos=(0, 0), size=(1.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
slider_a = visual.Slider(win=win, name='slider_a',
    size=(1.0, 0.05), pos=(0, -.15), units=None,
    labels=None, ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=0, style=('triangleMarker',),
    color='LightGray', font='HelveticaBold',
    flip=False)
scale_v = visual.ImageStim(
    win=win,
    name='scale_v',
    image='exp_data/img/SAM-V-9.png', mask=None,
    ori=0, pos=(0, -.3), size=(1.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
slider_v = visual.Slider(win=win, name='slider_v',
    size=(1.0, 0.05), pos=(0, -0.45), units=None,
    labels=None, ticks=(-4, -3, -2, -1, 0, 1, 2, 3, 4),
    granularity=0, style=('triangleMarker',),
    color='LightGray', font='HelveticaBold',
    flip=False)
key_resp_scales = keyboard.Keyboard()

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanks_text = visual.TextStim(win=win, name='thanks_text',
    text='The experiment is over.\nThank you for your participation!\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
welcomeComponents = [Welcome_text, key_resp]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
outlet.push_sample(x=[1])
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *Welcome_text* updates
    if Welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome_text.frameNStart = frameN  # exact frame index
        Welcome_text.tStart = t  # local t and not account for scr refresh
        Welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_text, 'tStartRefresh')  # time at next scr refresh
        Welcome_text.setAutoDraw(True)

    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Welcome_text.started', Welcome_text.tStartRefresh)
thisExp.addData('Welcome_text.stopped', Welcome_text.tStopRefresh)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "baseline"-------
continueRoutine = True
routineTimer.add(80.000000)
# update component parameters for each repeat
# keep track of which components have finished
baselineComponents = [instructions_text, image_01, image_02, image_03, image_04, image_05]
for thisComponent in baselineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
baselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "baseline"-------
outlet.push_sample(x=[2])
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = baselineClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=baselineClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instructions_text* updates
    if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.tStart = t  # local t and not account for scr refresh
        instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
        instructions_text.setAutoDraw(True)
    if instructions_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_text.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            instructions_text.tStop = t  # not accounting for scr refresh
            instructions_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_text, 'tStopRefresh')  # time at next scr refresh
            instructions_text.setAutoDraw(False)

    # *image_01* updates
    if image_01.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        image_01.frameNStart = frameN  # exact frame index
        image_01.tStart = t  # local t and not account for scr refresh
        image_01.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_01, 'tStartRefresh')  # time at next scr refresh
        image_01.setAutoDraw(True)
    if image_01.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_01.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image_01.tStop = t  # not accounting for scr refresh
            image_01.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_01, 'tStopRefresh')  # time at next scr refresh
            image_01.setAutoDraw(False)

    # *image_02* updates
    if image_02.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
        # keep track of start time/frame for later
        image_02.frameNStart = frameN  # exact frame index
        image_02.tStart = t  # local t and not account for scr refresh
        image_02.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_02, 'tStartRefresh')  # time at next scr refresh
        image_02.setAutoDraw(True)
    if image_02.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_02.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image_02.tStop = t  # not accounting for scr refresh
            image_02.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_02, 'tStopRefresh')  # time at next scr refresh
            image_02.setAutoDraw(False)

    # *image_03* updates
    if image_03.status == NOT_STARTED and tThisFlip >= 35-frameTolerance:
        # keep track of start time/frame for later
        image_03.frameNStart = frameN  # exact frame index
        image_03.tStart = t  # local t and not account for scr refresh
        image_03.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_03, 'tStartRefresh')  # time at next scr refresh
        image_03.setAutoDraw(True)
    if image_03.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_03.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image_03.tStop = t  # not accounting for scr refresh
            image_03.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_03, 'tStopRefresh')  # time at next scr refresh
            image_03.setAutoDraw(False)

    # *image_04* updates
    if image_04.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
        # keep track of start time/frame for later
        image_04.frameNStart = frameN  # exact frame index
        image_04.tStart = t  # local t and not account for scr refresh
        image_04.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_04, 'tStartRefresh')  # time at next scr refresh
        image_04.setAutoDraw(True)
    if image_04.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_04.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image_04.tStop = t  # not accounting for scr refresh
            image_04.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_04, 'tStopRefresh')  # time at next scr refresh
            image_04.setAutoDraw(False)

    # *image_05* updates
    if image_05.status == NOT_STARTED and tThisFlip >= 65-frameTolerance:
        # keep track of start time/frame for later
        image_05.frameNStart = frameN  # exact frame index
        image_05.tStart = t  # local t and not account for scr refresh
        image_05.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_05, 'tStartRefresh')  # time at next scr refresh
        image_05.setAutoDraw(True)
    if image_05.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_05.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image_05.tStop = t  # not accounting for scr refresh
            image_05.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_05, 'tStopRefresh')  # time at next scr refresh
            image_05.setAutoDraw(False)

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "baseline"-------
for thisComponent in baselineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_text.started', instructions_text.tStartRefresh)
thisExp.addData('instructions_text.stopped', instructions_text.tStopRefresh)
thisExp.addData('image_01.started', image_01.tStartRefresh)
thisExp.addData('image_01.stopped', image_01.tStopRefresh)
thisExp.addData('image_02.started', image_02.tStartRefresh)
thisExp.addData('image_02.stopped', image_02.tStopRefresh)
thisExp.addData('image_03.started', image_03.tStartRefresh)
thisExp.addData('image_03.stopped', image_03.tStopRefresh)
thisExp.addData('image_04.started', image_04.tStartRefresh)
thisExp.addData('image_04.stopped', image_04.tStopRefresh)
thisExp.addData('image_05.started', image_05.tStartRefresh)
thisExp.addData('image_05.stopped', image_05.tStopRefresh)

# ------Prepare to start Routine "fixation"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixationComponents = [fixation_cross]
for thisComponent in fixationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation"-------
outlet.push_sample(x=[3])
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *fixation_cross* updates
    if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_cross.frameNStart = frameN  # exact frame index
        fixation_cross.tStart = t  # local t and not account for scr refresh
        fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
        fixation_cross.setAutoDraw(True)
    if fixation_cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_cross.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            fixation_cross.tStop = t  # not accounting for scr refresh
            fixation_cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_cross, 'tStopRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(False)

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation"-------
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_cross.started', fixation_cross.tStartRefresh)
thisExp.addData('fixation_cross.stopped', fixation_cross.tStopRefresh)

# ------Prepare to start Routine "stimulus"-------
continueRoutine = True
routineTimer.add(203.000000)
# update component parameters for each repeat
# keep track of which components have finished
stimulusComponents = [movie]
for thisComponent in stimulusComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
stimulusClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "stimulus"-------
outlet.push_sample(x=[4])
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = stimulusClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=stimulusClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *movie* updates
    if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie.frameNStart = frameN  # exact frame index
        movie.tStart = t  # local t and not account for scr refresh
        movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
        movie.setAutoDraw(True)
    if movie.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > movie.tStartRefresh + 203-frameTolerance:
            # keep track of stop time/frame for later
            movie.tStop = t  # not accounting for scr refresh
            movie.frameNStop = frameN  # exact frame index
            win.timeOnFlip(movie, 'tStopRefresh')  # time at next scr refresh
            movie.setAutoDraw(False)

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in stimulusComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "stimulus"-------
for thisComponent in stimulusComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
movie.stop()

# ------Prepare to start Routine "Scale"-------
continueRoutine = True
# update component parameters for each repeat
slider_a.reset()
slider_v.reset()
key_resp_scales.keys = []
key_resp_scales.rt = []
_key_resp_scales_allKeys = []
# keep track of which components have finished
ScaleComponents = [scale_text, scale_a, slider_a, scale_v, slider_v, key_resp_scales]
for thisComponent in ScaleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ScaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Scale"-------
outlet.push_sample(x=[5])
while continueRoutine:
    # get current time
    t = ScaleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ScaleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *scale_text* updates
    if scale_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scale_text.frameNStart = frameN  # exact frame index
        scale_text.tStart = t  # local t and not account for scr refresh
        scale_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scale_text, 'tStartRefresh')  # time at next scr refresh
        scale_text.setAutoDraw(True)

    # *scale_a* updates
    if scale_a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scale_a.frameNStart = frameN  # exact frame index
        scale_a.tStart = t  # local t and not account for scr refresh
        scale_a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scale_a, 'tStartRefresh')  # time at next scr refresh
        scale_a.setAutoDraw(True)

    # *slider_a* updates
    if slider_a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_a.frameNStart = frameN  # exact frame index
        slider_a.tStart = t  # local t and not account for scr refresh
        slider_a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_a, 'tStartRefresh')  # time at next scr refresh
        slider_a.setAutoDraw(True)

    # *scale_v* updates
    if scale_v.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scale_v.frameNStart = frameN  # exact frame index
        scale_v.tStart = t  # local t and not account for scr refresh
        scale_v.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scale_v, 'tStartRefresh')  # time at next scr refresh
        scale_v.setAutoDraw(True)

    # *slider_v* updates
    if slider_v.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_v.frameNStart = frameN  # exact frame index
        slider_v.tStart = t  # local t and not account for scr refresh
        slider_v.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_v, 'tStartRefresh')  # time at next scr refresh
        slider_v.setAutoDraw(True)

    # *key_resp_scales* updates
    waitOnFlip = False
    if key_resp_scales.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_scales.frameNStart = frameN  # exact frame index
        key_resp_scales.tStart = t  # local t and not account for scr refresh
        key_resp_scales.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_scales, 'tStartRefresh')  # time at next scr refresh
        key_resp_scales.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_scales.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_scales.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_scales.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_scales.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_scales_allKeys.extend(theseKeys)
        if len(_key_resp_scales_allKeys):
            key_resp_scales.keys = _key_resp_scales_allKeys[-1].name  # just the last key pressed
            key_resp_scales.rt = _key_resp_scales_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ScaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Scale"-------
for thisComponent in ScaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('scale_text.started', scale_text.tStartRefresh)
thisExp.addData('scale_text.stopped', scale_text.tStopRefresh)
thisExp.addData('scale_a.started', scale_a.tStartRefresh)
thisExp.addData('scale_a.stopped', scale_a.tStopRefresh)
thisExp.addData('slider_a.response', slider_a.getRating())
thisExp.addData('slider_a.rt', slider_a.getRT())
thisExp.addData('slider_a.started', slider_a.tStartRefresh)
thisExp.addData('slider_a.stopped', slider_a.tStopRefresh)
thisExp.addData('scale_v.started', scale_v.tStartRefresh)
thisExp.addData('scale_v.stopped', scale_v.tStopRefresh)
thisExp.addData('slider_v.response', slider_v.getRating())
thisExp.addData('slider_v.rt', slider_v.getRT())
thisExp.addData('slider_v.started', slider_v.tStartRefresh)
thisExp.addData('slider_v.stopped', slider_v.tStopRefresh)
# the Routine "Scale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "thanks"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
thanksComponents = [thanks_text, key_resp_2]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
outlet.push_sample(x=[6])
while continueRoutine:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *thanks_text* updates
    if thanks_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks_text.frameNStart = frameN  # exact frame index
        thanks_text.tStart = t  # local t and not account for scr refresh
        thanks_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks_text, 'tStartRefresh')  # time at next scr refresh
        thanks_text.setAutoDraw(True)
    if thanks_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanks_text.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            thanks_text.tStop = t  # not accounting for scr refresh
            thanks_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanks_text, 'tStopRefresh')  # time at next scr refresh
            thanks_text.setAutoDraw(False)

    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks_text.started', thanks_text.tStartRefresh)
thisExp.addData('thanks_text.stopped', thanks_text.tStopRefresh)
# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
