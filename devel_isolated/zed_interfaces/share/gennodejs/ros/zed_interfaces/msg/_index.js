
"use strict";

let BoundingBox2Df = require('./BoundingBox2Df.js');
let Keypoint2Df = require('./Keypoint2Df.js');
let Keypoint2Di = require('./Keypoint2Di.js');
let RGBDSensors = require('./RGBDSensors.js');
let ObjectsStamped = require('./ObjectsStamped.js');
let Object = require('./Object.js');
let Keypoint3D = require('./Keypoint3D.js');
let BoundingBox2Di = require('./BoundingBox2Di.js');
let BoundingBox3D = require('./BoundingBox3D.js');
let Skeleton2D = require('./Skeleton2D.js');
let Skeleton3D = require('./Skeleton3D.js');
let PlaneStamped = require('./PlaneStamped.js');
let PosTrackStatus = require('./PosTrackStatus.js');

module.exports = {
  BoundingBox2Df: BoundingBox2Df,
  Keypoint2Df: Keypoint2Df,
  Keypoint2Di: Keypoint2Di,
  RGBDSensors: RGBDSensors,
  ObjectsStamped: ObjectsStamped,
  Object: Object,
  Keypoint3D: Keypoint3D,
  BoundingBox2Di: BoundingBox2Di,
  BoundingBox3D: BoundingBox3D,
  Skeleton2D: Skeleton2D,
  Skeleton3D: Skeleton3D,
  PlaneStamped: PlaneStamped,
  PosTrackStatus: PosTrackStatus,
};
