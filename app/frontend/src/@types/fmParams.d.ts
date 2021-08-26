export type fmParamsList = {
  [key: string]: fmParamsType;
};

export type fmParamsType = {
  atack: number;
  decay: number;
  sustain: number;
  release: number;
  frequency: number;
  // キャリア周波数に対するモジュレータの周波数の比率
  ratioToFoundamentalFrequency: number;
  //   変調指数
  modulationIndex: number;
};