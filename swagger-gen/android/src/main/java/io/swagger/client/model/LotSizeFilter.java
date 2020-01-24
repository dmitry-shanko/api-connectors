/**
 * Bybit API
 * ## REST API for the Bybit Exchange. Base URI: [https://api-testnet.bybit.com]  
 *
 * OpenAPI spec version: 1.0.0
 * Contact: support@bybit.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import io.swagger.annotations.*;
import com.google.gson.annotations.SerializedName;

@ApiModel(description = "")
public class LotSizeFilter {
  
  @SerializedName("min_trading_qty")
  private Object minTradingQty = null;
  @SerializedName("max_trading_qty")
  private Object maxTradingQty = null;
  @SerializedName("qty_step")
  private Object qtyStep = null;

  /**
   **/
  @ApiModelProperty(value = "")
  public Object getMinTradingQty() {
    return minTradingQty;
  }
  public void setMinTradingQty(Object minTradingQty) {
    this.minTradingQty = minTradingQty;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public Object getMaxTradingQty() {
    return maxTradingQty;
  }
  public void setMaxTradingQty(Object maxTradingQty) {
    this.maxTradingQty = maxTradingQty;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public Object getQtyStep() {
    return qtyStep;
  }
  public void setQtyStep(Object qtyStep) {
    this.qtyStep = qtyStep;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LotSizeFilter lotSizeFilter = (LotSizeFilter) o;
    return (this.minTradingQty == null ? lotSizeFilter.minTradingQty == null : this.minTradingQty.equals(lotSizeFilter.minTradingQty)) &&
        (this.maxTradingQty == null ? lotSizeFilter.maxTradingQty == null : this.maxTradingQty.equals(lotSizeFilter.maxTradingQty)) &&
        (this.qtyStep == null ? lotSizeFilter.qtyStep == null : this.qtyStep.equals(lotSizeFilter.qtyStep));
  }

  @Override
  public int hashCode() {
    int result = 17;
    result = 31 * result + (this.minTradingQty == null ? 0: this.minTradingQty.hashCode());
    result = 31 * result + (this.maxTradingQty == null ? 0: this.maxTradingQty.hashCode());
    result = 31 * result + (this.qtyStep == null ? 0: this.qtyStep.hashCode());
    return result;
  }

  @Override
  public String toString()  {
    StringBuilder sb = new StringBuilder();
    sb.append("class LotSizeFilter {\n");
    
    sb.append("  minTradingQty: ").append(minTradingQty).append("\n");
    sb.append("  maxTradingQty: ").append(maxTradingQty).append("\n");
    sb.append("  qtyStep: ").append(qtyStep).append("\n");
    sb.append("}\n");
    return sb.toString();
  }
}