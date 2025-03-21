import { Sequelize, DataTypes, Model } from 'sequelize';
import sequelize from '../database';
import Tickets from './Tickets';

const Users = sequelize.define(
    'users',
    {
        id: {
            type: DataTypes.INTEGER,
            autoIncrement: true,
            primaryKey: true,
        },
        username: {
            type: DataTypes.STRING,
            allowNull: false,
        },
        password: {
            type: DataTypes.STRING,
            allowNull: false,
        },
        firstName: {
            type: DataTypes.STRING,
            allowNull: false,
        },
        lastName: {
            type: DataTypes.STRING,
            allowNull: false,
        },
        email: {
            type: DataTypes.STRING,
            allowNull: false,
            unique: true,
        },
    },
    {
        timestamps: false, // Disable timestamps
    },
);

// Users.hasMany(Tickets, { foreignKey: 'buyer_id' });
// Tickets.belongsTo(Users, { foreignKey: 'buyer_id' });

export default Users;
