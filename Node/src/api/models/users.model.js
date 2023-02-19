const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const moment = require('moment-timezone');
const jwt = require('jwt-simple');

const {
  pwdSaltRounds,
  jwtExpirationInterval,
  pwEncryptionKey,
  uploadedImgPath
} = require('../../config/vars');

/**
 * User Schema
 * @private
 */
let UserSchema = new mongoose.Schema({
  userId:{type:Number, default:0, required:true,unique: true},
  type: { type: Number }, // 1 = Developer, 2 = Player
  username: { type: String },
  description: { type: String }, 
  email: { type: String, lowercase: true },
  password: { type: String },
  status:{type:Boolean,default:false},
  resetPasswordToken: { type: String },
  otp: { type: String },
  // imgs. with ipfs path
  profileImage: { type: String },
  bannerImage: { type: String },
  country:  {type:String},
  countryFlag:{type: String},
  shoutOut:{type: String},
  // imgs. saved on server
  profileImageLocal: { type: String },
  bannerImageLocal: { type: String },

  companyName:  { type: String },
  website: { type: String },
  designation: { type: String },
  walletAddress:{type: String },

  userWins: { type: String },    
  userLose: { type: String },
  deviceId: { type: String },


  facebookLink: { type: String },
  twitterLink: { type: String },
  gPlusLink: { type: String },
  vineLink: { type: String },
  signature: { type: String },   
  loginviaemail:{type:Boolean,default:false},
  ticket:{ type: String,default:'' },   
  dollar:{ type: String ,default:''},  
  deSkillzToken:{ type: String ,default:''},  

  loyaltyPoints: { type: Number,default: 0 }
   
}, { timestamps: true }
);

/**
 * Methods
 */



UserSchema.method({
  verifyPassword(password) {
    return bcrypt.compareSync(password, this.password);
  },
  transform() {
    const transformed = {};
    const fields = ['_id', 'email', 'description', 'facebookLink', 'gPlusLink', 'profileImage', 'profileImageLocal', 'bannerImage', 'bannerImageLocal', 'twitterLink', 'username', 'vineLink','userWins','userLose','deviceId','companyName','website','designation', 'status', 'loyaltyPoints'];

    fields.forEach((field) => {
      transformed[field] = this[field];
    });

    // asigning server path for images
    // transformed.profileImage = transformed.profileImageLocal ? `${uploadedImgPath}${transformed.profileImageLocal}` : ''
    // transformed.bannerImage = transformed.bannerImageLocal ? `${uploadedImgPath}${transformed.bannerImageLocal}` : ''

    // delete transformed.profileImageLocal
    // delete transformed.bannerImageLocal

    return transformed;
  },

  token() {
    const playload = {
      exp: moment().add(jwtExpirationInterval, 'minutes').unix(),
      iat: moment().unix(),
      sub: this._id,
    };
    return jwt.encode(playload, pwEncryptionKey);
  },
});

UserSchema.pre('save', async function save(next) {
  try {
    if (!this.isModified('password')) return next();
    const rounds = pwdSaltRounds ? parseInt(pwdSaltRounds) : 10;
    const hash = await bcrypt.hash(this.password, rounds);
    this.password = hash; 
    
    let user = await mongoose.model('User', UserSchema).findOne().limit(1).sort({$natural:-1})
    const userId= user ? user.userId : 0;
    this.userId = userId+1;

    return next();
  }
  catch (error) {
    return next(error);
  }
});

UserSchema.pre('findOneAndUpdate', async function (next) {
  try{
    const rounds = pwdSaltRounds ? parseInt(pwdSaltRounds) : 10;
    if(this._update['$set']?.password) {
      const hash = await bcrypt.hash(this._update['$set']?.password, rounds);
      this._update.password = hash;
    }
    return next();
  }
  catch (e) {
    return next(e);
  }
});

/**
 * @typedef User
 */

module.exports = mongoose.model('User', UserSchema);