//
// RiskIDRes.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation


/** Set risk limit. */

public struct RiskIDRes: Codable {

    public var _id: Double?
    public var coin: String?
    public var limit: Double?
    public var maintainMargin: String?
    public var startingMargin: String?
    public var section: String?
    public var isLowestRisk: Double?
    public var createdAt: String?
    public var updatedAt: String?

    public init(_id: Double?, coin: String?, limit: Double?, maintainMargin: String?, startingMargin: String?, section: String?, isLowestRisk: Double?, createdAt: String?, updatedAt: String?) {
        self._id = _id
        self.coin = coin
        self.limit = limit
        self.maintainMargin = maintainMargin
        self.startingMargin = startingMargin
        self.section = section
        self.isLowestRisk = isLowestRisk
        self.createdAt = createdAt
        self.updatedAt = updatedAt
    }

    public enum CodingKeys: String, CodingKey { 
        case _id = "id"
        case coin
        case limit
        case maintainMargin = "maintain_margin"
        case startingMargin = "starting_margin"
        case section
        case isLowestRisk = "is_lowest_risk"
        case createdAt = "created_at"
        case updatedAt = "updated_at"
    }


}

