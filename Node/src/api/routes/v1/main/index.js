const express = require('express')

const attendenceRoutes = require('./attendence.route')
const router = express.Router()
const {uploadToCloudinary,cpUpload}=require('../../../utils/upload')
/**
 * GET v1/status
 */
router.use('/attendence', attendenceRoutes)


module.exports = router
